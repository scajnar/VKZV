import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-rent-or',
  templateUrl: './rent-or.component.html',
  styleUrls: ['./rent-or.component.scss']
})
export class RentOrComponent implements OnInit {

  constructor() { }

  newUser : any;

  ngOnInit(): void {
  }
  addNewUser(){
    if(this.newUser != null && this.newUser.length != 0){
      //klic na bazo za dodajanje novega userja
    }
  }
}
