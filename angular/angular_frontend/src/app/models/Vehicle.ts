export class Vehicle{
  id : any;
  Type: string;
  Name: String;
  Brand: String;
  Model: String;
  Horsepower: number;

  constructor(id:any, Type: string, Name: String, Brand: String, Model: String, Horsepower: number) {
    this.id = id;
    this.Type = Type;
    this.Name = Name;
    this.Brand = Brand;
    this.Model = Model;
    this.Horsepower = Horsepower;
  }
}
