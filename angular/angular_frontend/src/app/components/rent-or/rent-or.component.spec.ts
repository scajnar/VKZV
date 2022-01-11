import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RentOrComponent } from './rent-or.component';

describe('RentOrComponent', () => {
  let component: RentOrComponent;
  let fixture: ComponentFixture<RentOrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RentOrComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RentOrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
