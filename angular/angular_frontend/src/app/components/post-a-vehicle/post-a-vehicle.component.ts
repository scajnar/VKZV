import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {Vehicle} from "../../models/Vehicle";
import {BackendService} from "../../services/backend.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-post-a-vehicle',
  templateUrl: './post-a-vehicle.component.html',
  styleUrls: ['./post-a-vehicle.component.scss']
})
export class PostAVehicleComponent implements OnInit {

  public vehicleForm: FormGroup = new FormGroup({
    Type: new FormControl("", Validators.required),
    Name: new FormControl("", Validators.required),
    Brand: new FormControl("", Validators.required),
    Model: new FormControl("", Validators.required),
    Horsepower: new FormControl("", Validators.required),
    Price: new FormControl("", Validators.required),
    Location: new FormControl("", Validators.required),
  })

  constructor(private service: BackendService, private router: Router){}

  id: any;
  ngOnInit(): void {
    this.service.id.subscribe(data => {
      this.id = data;
    });
  }

  postVehicle() {
    this.vehicleForm.markAllAsTouched();
    if (this.vehicleForm.valid) {
      this.service.postAVehicle(
        this.vehicleForm.value.Name,
        this.vehicleForm.value.Brand,
        this.vehicleForm.value.Model,
        this.vehicleForm.value.Horsepower)
        .subscribe(data => {
          this.service.postAListing(data,new Date(),new Date(),this.id,this.vehicleForm.value.Price,this.vehicleForm.value.Location).subscribe();
          this.router.navigateByUrl("")
        })



    }

  }

}4
