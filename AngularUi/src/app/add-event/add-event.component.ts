import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-event',
  templateUrl: './add-event.component.html',
  styleUrls: ['./add-event.component.css']
})
export class AddEventComponent implements OnInit {
  newEvent: any = {};
  constructor(
    private http:HttpClient,
    private router:Router,
  ) { }

  ngOnInit(): void {
  }

  addEvent() {
    console.log(this.newEvent)
    this.http.post('http://127.0.0.1:8000/api/create_event', this.newEvent).subscribe(data => {
      console.log(data);
      this.router.navigate(['/events']);


    });
  }

}
