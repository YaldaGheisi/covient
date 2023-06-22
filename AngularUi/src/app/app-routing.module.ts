import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddEventComponent } from './add-event/add-event.component';
import { EventComponent } from './event/event.component';
import {HomeComponent} from './home/home.component';
import {LoginComponent} from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import {RegisterComponent} from './register/register.component';
import { UserComponent } from './user/user.component';

const routes: Routes = [
  {path: '', component:LoginComponent},
  {path: 'login', component:LoginComponent},
  {path: 'register', component:RegisterComponent},
  {path: 'user', component:UserComponent},
  {path: 'events', component:EventComponent},
  {path: 'profile', component:ProfileComponent},
  {path: 'add_event', component:AddEventComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
