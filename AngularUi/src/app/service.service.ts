import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(
    private _http:HttpClient
  ) { }

  getUserData(){
    return this._http.get('http://127.0.0.1:8000/api/user', {withCredentials:true});
  }

  getEventData(){
    return this._http.get('http://127.0.0.1:8000/api/events', {withCredentials:false});
  }


}
