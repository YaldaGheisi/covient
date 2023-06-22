import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';



@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: FormGroup;

  constructor(
    private formBuilder:FormBuilder,
    private http:HttpClient,
    private router:Router) { }

  ngOnInit(): void {
    this.form = this.formBuilder.nonNullable.group(
     {
      first_name:"",
      last_name:"",
      email:"",
      password:"",
      address:"",



    }
    );
  }

  submitRegistration(): void{
    console.log(this.form.getRawValue());
    this.http.post('http://127.0.0.1:8000/api/register', this.form.getRawValue()).subscribe(
      ()=> this.router.navigate(['/login'])
      // res => {console.log(res); }
    );
  }

  uploadFile() {
    const formData = new FormData();
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
    const fileName = document.getElementById('fileName');
    formData.append('file', fileInput.files[0]);
    fileName.innerHTML = fileInput.files[0].name;
    this.http.post('http://localhost:8000/api/register_from_csv', formData).subscribe(
      response => console.log(response),
      error => console.log(error)
    );
  }

  displayFileName() {
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
    const fileName = document.getElementById('fileName');

    fileName.innerHTML = fileInput.files[0].name;
  }




}
