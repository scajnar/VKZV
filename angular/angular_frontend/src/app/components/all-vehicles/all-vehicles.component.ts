import { Component, OnInit } from '@angular/core';
import {Vehicle} from "../../models/Vehicle";
import {Router} from "@angular/router";

@Component({
  selector: 'app-all-vehicles',
  templateUrl: './all-vehicles.component.html',
  styleUrls: ['./all-vehicles.component.scss']
})
export class AllVehiclesComponent implements OnInit {

  constructor(private router: Router) { }

  temp = [
    new Vehicle(1,"bike","penis","model1","asd",66),
    new Vehicle(2,"car","penisdd","model2","asd",66),
    new Vehicle(3,"bike","penisss","model3","asd",66),
  ]
  ngOnInit(): void {
  }

  viewVehicle(car: any){
    this.router.navigateByUrl("/view/" + car.id)
  }

}
