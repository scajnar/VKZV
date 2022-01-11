import { Component, OnInit } from '@angular/core';
import {BackendService} from "../../services/backend.service";

@Component({
  selector: 'app-rent-or',
  templateUrl: './rent-or.component.html',
  styleUrls: ['./rent-or.component.scss']
})
export class RentOrComponent implements OnInit {

  constructor(private service: BackendService) { }

  canPost = true;
  newUser : any;

  ngOnInit(): void {
  }
  addNewUser(){
    if(this.newUser != null && this.newUser.length != 0){
      //klic na bazo za dodajanje novega userja
      this.service.createWallet(this.newUser).subscribe(data => this.service.nextId(data))
      this.canPost = false;

    }
  }

}
