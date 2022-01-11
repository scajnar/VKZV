export class Vehicle{
  Type: string;
  Name: String;
  Brand: String;
  Model: String;
  Horsepower: number;

  constructor(Type: string, Name: String, Brand: String, Model: String, Horsepower: number) {
    this.Type = Type;
    this.Name = Name;
    this.Brand = Brand;
    this.Model = Model;
    this.Horsepower = Horsepower;
  }
}
