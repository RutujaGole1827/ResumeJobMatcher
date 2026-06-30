import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = "http://127.0.0.1:8001/api/resume";

  constructor(private http: HttpClient) {}

  uploadResume(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  return this.http.post("http://127.0.0.1:8001/api/resume/upload", formData);
}
  
}