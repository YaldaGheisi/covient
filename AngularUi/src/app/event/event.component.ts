import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import{ServiceService} from '../service.service';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css']
})
export class EventComponent implements OnInit {
  event_data:any;
  showAddEventForm: boolean = false;
  newEvent: any = {};
  constructor(
    private formBuilder:FormBuilder,
    private http:HttpClient,
    private router:Router,
    private _service:ServiceService,
    private authService: AuthService, // inject the AuthService here
  ) { }

  // ngOnInit(): void {
  //   this._service.getEventData().subscribe(
  //     res=> {this.event_data = res;}
  //   );
  //   console.log(this.event_data);

  // }
  ngOnInit(): void {
    if (this.authService.isLoggedIn()) { // check if the user is logged in
      console.log("Hey! user is logged in")
      this._service.getEventData().subscribe(
        res => {
          this.event_data = res;
        }
      );
    } else {
      console.log("Hey! user is NOT logged in")
      this.router.navigate(['/login']); // redirect to the login page if the user is not logged in
    }
  }


  openAddEventForm() {
    // this.showAddEventForm = true;
    this.router.navigate(['/add_event']);
  }

  addEvent() {
    console.log(this.newEvent)
    this.http.post('http://127.0.0.1:8000/api/create_event', this.newEvent).subscribe(data => {
      console.log(data);
      this.showAddEventForm = false;
      // this.newEvent = {};
      this._service.getEventData();
      window.location.reload();
    });
  }

  deleteEvent(eventId) {
    if (confirm("Are you sure you want to delete this event?")) {
      fetch(`http://127.0.0.1:8000/api/delete_event/${eventId}/`, {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include'
      })
      .then(response => {
        if (response.ok) {
          window.location.reload();  // Reload the page after successful deletion
        } else {
          alert('Failed to delete event');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
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





}
