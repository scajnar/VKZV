import { Component, OnInit } from '@angular/core';
import {BackendService} from "../../services/backend.service";

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {

  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    this.backendService.getWallets().subscribe(data =>{
      console.log(data)
    })
  }

}
