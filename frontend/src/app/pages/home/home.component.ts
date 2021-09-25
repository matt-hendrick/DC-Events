import { Component, OnInit } from '@angular/core';

import { Event } from '../../event.interface';
import { EventService } from '../../services/event.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  private events: Event[] = [];
  filters: Set<string> = new Set();

  get displayedEvents(): Event[] {
    if (this.filters.size < 1) return this.events;
    else {
      return this.events.filter((event) => !this.filters.has(event.type));
    }
  }
  constructor(private eventService: EventService) {}

  ngOnInit(): void {
    this.onGetEvents();
  }

  onGetEvents(): void {
    this.eventService
      .getEvents()
      .subscribe((events: Event[]) => (this.events = events));
  }

  toggleFilters(entityType: string): void {
    if (!this.filters.has(entityType)) this.filters.add(entityType);
    else this.filters.delete(entityType);
  }

  clearFilters(): void {
    if (this.filters.size > 0) this.filters = new Set();
  }
}
