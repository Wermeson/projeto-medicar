import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-medico-crud',
  templateUrl: './medico-crud.component.html',
  styleUrls: ['./medico-crud.component.css']
})
export class MedicoCrudComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  navigateToMedicoCreate(): void {
    this.router.navigate(['/medico/create'])
  }
}
