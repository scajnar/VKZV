import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {BehaviorSubject, Observable, throwError} from 'rxjs';
import {API_URL} from '../env';
import {Wallet} from "../models/wallet";

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  car:BehaviorSubject<any>=new BehaviorSubject<any>(null)
  id:BehaviorSubject<any>=new BehaviorSubject<any>(null)
  listingId:BehaviorSubject<any>=new BehaviorSubject<any>(null)

  constructor(private http: HttpClient) { }

  nextCar(car:any){
    this.car.next(car)
  }
  nextId(id:any){
    this.id.next(id)
  }

  nextListingId(id:any){
    this.listingId.next(id)
  }
  createWallet(name:string){
    console.log("jbem ti mattr")
    return this.http.post(`${API_URL}/wallet/`+name, null)
  }
  getWallets() {
    return this.http.get(`${API_URL}/wallet`)
  }

  getAllVehicles(){
    return this.http.get(`${API_URL}/vehicles/`)
  }

  getVehicleById(id:number){
    return this.http.get(`${API_URL}/vehicles/`+id)
  }

  postAVehicle(name:string, brand:string, model:string, horsepower:number){
    return this.http.post(`${API_URL}/vehicle/`+name+"/"+brand+"/"+model+"/"+"/"+horsepower, null)
  }

  postAListing(vehicle_id:any, time_of_sharing: any, listing_time:any, user_id:number, price:number, location:string){
    return this.http.post(`${API_URL}/listing/`+vehicle_id+"/"+time_of_sharing+"/"+listing_time+"/"+"/"+user_id+"/"+price+"/"+location, null)
  }

  claimAlisting(listing_id:number, claiming_user_id:number){
    return this.http.post(`${API_URL}/listing/claim/`+listing_id+"/"+claiming_user_id,null)
  }

  getAllListing(){
    return this.http.get(`${API_URL}/listings`)
  }
}
