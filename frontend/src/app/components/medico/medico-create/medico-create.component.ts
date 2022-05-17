import { EspecialidadeService } from "./../../especialidades/especialidade.service";
import { MedicoService } from "./../medico.service";
import { Especialidade } from "./../../especialidades/especialidade.model";
import { Medico } from "./../medico.model";
import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";

@Component({
  selector: "app-medico-create",
  templateUrl: "./medico-create.component.html",
  styleUrls: ["./medico-create.component.css"],
})
export class MedicoCreateComponent implements OnInit {
  medico: Medico = {
    nome: "",
    crm: "",
    email: "",
    telefone: "",
    especialidade_id: 0,
  };
  especialidades: Especialidade[] = [];

  constructor(
    private medicoService: MedicoService,
    private router: Router,
    private especialidadeService: EspecialidadeService
  ) {}

  ngOnInit(): void {
    this.especialidadeService.read().subscribe((especialidades) => {
      this.especialidades = especialidades;
    });
  }

  createMedico(): void {
    this.medicoService.create(this.medico).subscribe(() => {
      this.medicoService.showMessage("Médico cadastrado com sucesso.");
      this.router.navigate(["/medicos"]);
    });
  }

  cancel(): void {
    this.router.navigate(["/medicos"]);
  }
}
