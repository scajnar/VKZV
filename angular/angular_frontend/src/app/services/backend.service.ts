import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {API_URL} from '../env';
import {Wallet} from "../models/wallet";

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private http: HttpClient) { }

  getWallets() {
    return this.http.get(`${API_URL}/wallet`)
  }
}
