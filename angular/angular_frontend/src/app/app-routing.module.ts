import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PostAVehicleComponent} from "./components/post-a-vehicle/post-a-vehicle.component";
import {RentOrComponent} from "./components/rent-or/rent-or.component";
import {AllVehiclesComponent} from "./components/all-vehicles/all-vehicles.component";
import {ViewVehicleComponent} from "./components/view-vehicle/view-vehicle.component";

const routes: Routes = [
  { path: '', component: RentOrComponent },
  { path: 'post', component: PostAVehicleComponent },
  { path: 'all', component: AllVehiclesComponent },
  { path: 'view/:id', component: ViewVehicleComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
