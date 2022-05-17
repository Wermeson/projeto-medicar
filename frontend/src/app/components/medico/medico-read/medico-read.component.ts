import { Especialidade } from './../../especialidades/especialidade.model';
import { EspecialidadeService } from './../../especialidades/especialidade.service';
import { MedicoService } from './../medico.service';
import { Medico } from './../medico.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-medico-read',
  templateUrl: './medico-read.component.html',
  styleUrls: ['./medico-read.component.css']
})
export class MedicoReadComponent implements OnInit {

  medicos: Medico[] = []
  especialidade: Especialidade[] = []
  displayedColumns = ['id', 'nome', 'crm', 'especialidade']

  constructor(private medicoService: MedicoService, private especialidadeService: EspecialidadeService) { }

  ngOnInit(): void {
    this.medicoService.read().subscribe(medicos => {
      this.medicos = medicos
    })
    this.getEspecialidadeById(5)
  }

  getEspecialidadeById(id:number){
    this.especialidadeService.getEspecialidade(id).subscribe(especialidade => {
      this.especialidade = especialidade
      return this.especialidade
    })
  }
}
