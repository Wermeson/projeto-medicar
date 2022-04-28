import { EspecialidadeService } from './../especialidade.service';
import { Especialidade } from './../especialidade.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-especialidades-read',
  templateUrl: './especialidades-read.component.html',
  styleUrls: ['./especialidades-read.component.css']
})
export class EspecialidadesReadComponent implements OnInit {

  especialidades: Especialidade[] = []
  displayedColumns = ['id', 'nome', 'action']

  constructor(private especialidadeService: EspecialidadeService) { }

  ngOnInit(): void {
    this.especialidadeService.read().subscribe(especialidades => {
      this.especialidades = especialidades
    })
  }

}
