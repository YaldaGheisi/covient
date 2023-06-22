import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  constructor(
    private http:HttpClient,
    private router:Router,
    public authService: AuthService
  ) { }

  ngOnInit(): void {


  }

  onLogout():void{
    this.http.get('http://127.0.0.1:8000/api/logout', {withCredentials:true} ).subscribe(
      ()=> this.router.navigate(['/login'])
    );
    this.authService.logout();
  }

}
