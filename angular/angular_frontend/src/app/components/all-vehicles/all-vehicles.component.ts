import { Component, OnInit } from '@angular/core';
import {Vehicle} from "../../models/Vehicle";
import {Router} from "@angular/router";
import {BackendService} from "../../services/backend.service";

@Component({
  selector: 'app-all-vehicles',
  templateUrl: './all-vehicles.component.html',
  styleUrls: ['./all-vehicles.component.scss']
})
export class AllVehiclesComponent implements OnInit {

  constructor(private service: BackendService, private router: Router){}
  temp:any;
  allListings:any;
  ngOnInit(): void {
    this.service.getAllVehicles().subscribe(res=>{this.temp=res})
    this.service.getAllListing().subscribe(res=> {
      this.allListings = res;
    })
  }

  viewVehicle(car: any){
    for(let i = 0; i < this.allListings.length; i++){
      if(this.allListings[i].vehicle == car.id_number){
        console.log(this.allListings[i].id_number)
        console.log(car)
        this.service.nextListingId(this.allListings[i].id_number)
        this.service.nextCar(car)
        this.router.navigateByUrl("/view/" + car.id)
      }
    }


  }

}
