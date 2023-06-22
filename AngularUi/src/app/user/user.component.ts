import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import{ServiceService} from '../service.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  user_data:any;
  constructor(
    private formBuilder:FormBuilder,
    private http:HttpClient,
    private router:Router,
    private _service:ServiceService
  ) { }

  ngOnInit(): void {
    this._service.getUserData().subscribe(
      res=> {this.user_data = res;}
    );
    console.log(this.user_data);
  }

}
