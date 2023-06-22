import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;
  incorrect: boolean = false;
  constructor(
    private formBuilder:FormBuilder,
    private http:HttpClient,
    private router:Router,
    public authService: AuthService
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.nonNullable.group(
      {
       email:"",
       password:""
     }
     );
  }

  // submit():void{
  //   console.log(this.form.getRawValue());
  //   this.http.post('http://127.0.0.1:8000/api/login', this.form.getRawValue(), {withCredentials:true} ).subscribe(
  //     ()=> this.router.navigate(['/user'])
  //   );
  //   this.authService.login();
  // }
  submit(): void {
    console.log(this.form.getRawValue());
    this.http.post('http://127.0.0.1:8000/api/login', this.form.getRawValue(), { withCredentials: true }).subscribe(
      () => {
        this.router.navigate(['/user']);
        this.authService.login();
      },
      error => {
        console.error('Login failed:', error);
        this.router.navigate(['/login']);
        this.incorrect = true;
        // handle the error here (e.g. display an error message to the user)
      }
    );
  }



}

