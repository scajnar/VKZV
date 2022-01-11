import { Component, OnInit } from '@angular/core';
import {Vehicle} from "../../models/Vehicle";
import {BackendService} from "../../services/backend.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-view-vehicle',
  templateUrl: './view-vehicle.component.html',
  styleUrls: ['./view-vehicle.component.scss']
})
export class ViewVehicleComponent implements OnInit {

  constructor(private service: BackendService, private router: Router){}
  temp:any;
  listing_id: any;
  user_id: any;
  ngOnInit(): void {
    this.service.car.subscribe(data=>{
      this.temp=data
      console.log(this.temp)
    })
    this.service.id.subscribe(data=>{
      this.user_id=data
    })
    this.service.listingId.subscribe(data=>{
      this.listing_id=data
    })
  }

  borrowVehicle(){
    console.log(this.user_id)
    console.log(this.listing_id)
    this.service.claimAlisting(this.listing_id,this.user_id).subscribe()
    this.router.navigateByUrl('')
  }
}
