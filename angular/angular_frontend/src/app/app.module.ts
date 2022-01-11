import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TestComponent } from './components/test/test.component';
import { HttpClientModule } from '@angular/common/http';
import { RentOrComponent } from './components/rent-or/rent-or.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonToggleModule} from "@angular/material/button-toggle";
import {MatButtonModule} from "@angular/material/button";
import { PostAVehicleComponent } from './components/post-a-vehicle/post-a-vehicle.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { AllVehiclesComponent } from './components/all-vehicles/all-vehicles.component';
import { ViewVehicleComponent } from './components/view-vehicle/view-vehicle.component';

@NgModule({
  declarations: [
    AppComponent,
    TestComponent,
    RentOrComponent,
    PostAVehicleComponent,
    AllVehiclesComponent,
    ViewVehicleComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonToggleModule,
    MatButtonModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
