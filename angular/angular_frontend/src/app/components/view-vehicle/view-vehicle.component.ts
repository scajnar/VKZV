import { Component, OnInit } from '@angular/core';
import {Vehicle} from "../../models/Vehicle";

@Component({
  selector: 'app-view-vehicle',
  templateUrl: './view-vehicle.component.html',
  styleUrls: ['./view-vehicle.component.scss']
})
export class ViewVehicleComponent implements OnInit {

  constructor() { }

  temp = [
    new Vehicle(1,"bike","penis","model1","asd",66),
    new Vehicle(2,"car","penisdd","model2","asd",66),
    new Vehicle(3,"bike","penisss","model3","asd",66),
  ]

  ngOnInit(): void {
  }

  borrowVehicle(){

  }

}
