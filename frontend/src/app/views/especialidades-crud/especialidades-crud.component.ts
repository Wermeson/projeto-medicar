import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-especialidades-crud',
  templateUrl: './especialidades-crud.component.html',
  styleUrls: ['./especialidades-crud.component.css']
})
export class EspecialidadesCrudComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  navigateToEspecialidadesCreate(): void {
    this.router.navigate(['/especialidades/create'])
  }
}
