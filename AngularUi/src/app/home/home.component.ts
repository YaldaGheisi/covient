import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  message = "You are not logged in";

  constructor(
    private http:HttpClient,
    private router:Router

  ) { }

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:8000/api/user', {withCredentials:true}).subscribe(
       res =>{
        this.message = "Successfully Logged In";
        console.log(res);
    }
      );
  }

  onLogout():void{
    this.http.get('http://127.0.0.1:8000/api/logout', {withCredentials:true} ).subscribe(
      ()=> this.router.navigate(['/login'])
    );


  }

}
