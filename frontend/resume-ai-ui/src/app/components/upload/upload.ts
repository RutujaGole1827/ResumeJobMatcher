import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './upload.html',
  styleUrls: ['./upload.css'],
})

export class UploadComponent {
  responseData: any = null;
  loading = false;

  selectedFile: File | null = null;

isNumber(val: any): boolean {
  return typeof val === 'number';
}

  constructor(
  private api: ApiService,
  private cd: ChangeDetectorRef
) {}

  onFileSelect(event: any) {
    this.selectedFile = event.target.files[0];
    console.log("File selected:", this.selectedFile);
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer?.files.length) {
      this.selectedFile = event.dataTransfer.files[0];
      console.log("File dropped:", this.selectedFile);
    }
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
  }
  
calculateScore(jobMatches: any): number {
  const values = Object.values(jobMatches).map((v: any) =>
    typeof v === 'number' ? v : v.score ?? v.match ?? 0
  );

  if (!values.length) return 0;

  const avg = values.reduce((a, b) => a + b, 0) / values.length;

  return Math.round(avg * 100);
}
  upload() {
  if (!this.selectedFile) return;

  this.loading = true;
  this.responseData = null;

  this.api.uploadResume(this.selectedFile).subscribe({
    next: (res: any) => {

      const score = this.calculateScore(res.job_matches);

      this.responseData = {
        skills: res.skills_found,
        experience: res.experience_years,
        job_matches: Object.entries(res.job_matches).map(([key, value]: any) => {
          return {
            role: key,
            score: typeof value === 'number'
              ? value
              : value.score ?? value.match ?? value.value ?? 0
          };
        }),
        match_score: score
      };

      setTimeout(() => {
        this.loading = false;
        this.cd.detectChanges();
      }, 500);

    },

    error: (err: any) => {
      console.error(err);
      this.loading = false;
    }
  });
}

}