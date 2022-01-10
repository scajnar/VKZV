export class Wallet {
  name: string;
  id: number;
  balance : number;


  constructor(name: string, id: number, balance: number) {
    this.name = name;
    this.id = id;
    this.balance = balance;
  }
}
