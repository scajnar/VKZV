import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {Vehicle} from "../../models/Vehicle";

@Component({
  selector: 'app-post-a-vehicle',
  templateUrl: './post-a-vehicle.component.html',
  styleUrls: ['./post-a-vehicle.component.scss']
})
export class PostAVehicleComponent implements OnInit {

  public vehicleForm: FormGroup = new FormGroup({
    Type : new FormControl("",Validators.required),
    Name : new FormControl("",Validators.required),
    Brand : new FormControl("",Validators.required),
    Model : new FormControl("",Validators.required),
    Horsepower : new FormControl("",Validators.required),
  })

  constructor() { }

  ngOnInit(): void {
  }

  postVehicle(){
    this.vehicleForm.markAllAsTouched();
    if(this.vehicleForm.valid){
      const newVehicle = new Vehicle(
        null,
        this.vehicleForm.value.Type,
        this.vehicleForm.value.Name,
        this.vehicleForm.value.Brand,
        this.vehicleForm.value.Model,
        this.vehicleForm.value.Horsepower)
      console.log(newVehicle)
    }
  }

}
