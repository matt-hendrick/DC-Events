import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EventService } from 'src/app/services/event.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { HomeComponent } from './home.component';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { MOCK_EVENTS } from '../../mock-events';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;
  let compiled: HTMLElement;

  let eventServiceStub: any;

  beforeEach(async () => {
    eventServiceStub = {
      getEvents(): Observable<any> {
        return of(MOCK_EVENTS);
      },
    };

    await TestBed.configureTestingModule({
      declarations: [HomeComponent],
      providers: [{ provide: EventService, useValue: eventServiceStub }],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    compiled = fixture.nativeElement;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should render 3 event cards and displayedEvents should contain mock event data', () => {
    expect(compiled.querySelectorAll('app-card').length).toEqual(3);
    expect(component.displayedEvents.length).toEqual(3);
    expect(component.displayedEvents[0].entity).toEqual(MOCK_EVENTS[0].entity);
  });

  it('should render 4 buttons', () => {
    expect(compiled.querySelectorAll('button').length).toEqual(4);
  });
});
