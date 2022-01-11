import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostAVehicleComponent } from './post-a-vehicle.component';

describe('PostAVehicleComponent', () => {
  let component: PostAVehicleComponent;
  let fixture: ComponentFixture<PostAVehicleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostAVehicleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostAVehicleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
