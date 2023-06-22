import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { tap } from 'rxjs/operators';


@Injectable({providedIn: 'root'})
export class AuthService {
  public isLoggedIn$: BehaviorSubject<boolean>;
  private isAuthenticated = false;
  currentUser: any;

  constructor(
    private http: HttpClient,
    private router: Router
    ) {
    const isLoggedIn = localStorage.getItem('loggedIn') === 'true';
    this.isLoggedIn$ = new BehaviorSubject(isLoggedIn);
  }

  login() {
    // logic
    localStorage.setItem('loggedIn', 'true');
    this.isLoggedIn$.next(true);
    this.isAuthenticated = true;


  }

  logout() {
    // logic
    localStorage.setItem('loggedIn', 'false');
    this.isLoggedIn$.next(false);
    this.isAuthenticated = false;
  }

  isAuthenticatedUser() {
    return this.isAuthenticated;
  }

  isLoggedIn(): boolean {
    console.log("isLoggedIn() called")
    return localStorage.getItem('loggedIn') === 'true'
  }


}