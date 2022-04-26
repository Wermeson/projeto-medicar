import { EspecialidadesCreateComponent } from './components/especialidades/especialidades-create/especialidades-create.component';
import { EspecialidadesCrudComponent } from './views/especialidades-crud/especialidades-crud.component';
import { HomeComponent } from './views/home/home.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
  path: "",
    component: HomeComponent
  },
  {
    path: "especialidades",
    component: EspecialidadesCrudComponent
  },
  {
    path: "especialidades/create",
    component: EspecialidadesCreateComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
