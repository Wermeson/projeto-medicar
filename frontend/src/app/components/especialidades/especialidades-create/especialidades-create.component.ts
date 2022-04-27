import { Especialidade } from './../especialidade.model';
import { EspecialidadeService } from './../especialidade.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-especialidades-create',
  templateUrl: './especialidades-create.component.html',
  styleUrls: ['./especialidades-create.component.css']
})
export class EspecialidadesCreateComponent implements OnInit {

  especialidade: Especialidade = {
    nome: 'Teste 2'
  }

  constructor(private especialidadeService: EspecialidadeService, private router: Router) { }

  ngOnInit(): void {
    
  }

  createEspecialidade(): void {
    this.especialidadeService.create(this.especialidade).subscribe(()=> {
      this.especialidadeService.showMessage('Especialidade cadastrada com sucesso.');
      this.router.navigate(['/especialidades']);
    })
    
  }

  cancel(): void {
    this.router.navigate(['/especialidades']);
  }
}
