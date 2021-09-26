import {
  ComponentFixture,
  fakeAsync,
  TestBed,
  tick,
} from '@angular/core/testing';
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

  it('should render event card for each event in MOCK_EVENTS and displayedEvents should contain mock event data', () => {
    expect(compiled.querySelectorAll('app-card').length).toEqual(
      MOCK_EVENTS.length
    );
    expect(component.displayedEvents.length).toEqual(MOCK_EVENTS.length);
    expect(component.displayedEvents[0].entity).toEqual(MOCK_EVENTS[0].entity);
  });

  it('toggleFilters and clearFilters properly filter out cards displayed', () => {
    // Verifying that no filters are added and all cards are initially displayed
    expect(component.filters.size).toBe(0);
    expect(component.displayedEvents.length).toEqual(MOCK_EVENTS.length);

    // Testing that each of the filters removes the correct number of cards and is added to filter set
    component.toggleFilters('Bookstore');
    expect(component.filters.size).toBe(1);
    expect(component.displayedEvents.length).toEqual(2);

    component.toggleFilters('Newspaper');
    expect(component.filters.size).toBe(2);
    expect(component.displayedEvents.length).toEqual(1);

    component.toggleFilters('Think Tank');
    expect(component.filters.size).toBe(3);
    expect(component.displayedEvents.length).toEqual(0);

    // testing that removing a filter from the set works properly
    component.toggleFilters('Bookstore');
    expect(component.filters.size).toBe(2);
    expect(component.displayedEvents.length).toEqual(2);

    // testing that clearFilters resets everything properly
    component.clearFilters();
    expect(component.filters.size).toBe(0);
    expect(component.displayedEvents.length).toEqual(MOCK_EVENTS.length);
  });

  it('should render 4 buttons', () => {
    expect(compiled.querySelectorAll('button').length).toEqual(4);
  });

  it('button click on filters runs toggleFilter func', fakeAsync(() => {
    spyOn(component, 'toggleFilters');
    let bookStoreFilterButton = compiled.querySelector(
      '#bookstore-filter-button'
    ) as HTMLButtonElement;
    bookStoreFilterButton.click();
    tick();
    expect(component.toggleFilters).toHaveBeenCalled();
  }));
});
