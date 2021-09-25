import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Event } from '../../event.interface';
import { EventService } from '../../services/event.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  events?: Event[];

  constructor(private eventService: EventService) {}

  ngOnInit(): void {
    this.onGetEvents();
  }

  onGetEvents(): void {
    this.eventService
      .getEvents()
      .subscribe((response) => (this.events = response.body.Items));
  }
}
