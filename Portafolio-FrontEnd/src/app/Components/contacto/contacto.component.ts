import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-contacto',
  templateUrl: './contacto.component.html',
  styleUrls: ['./contacto.component.css']
})
export class ContactoComponent implements OnInit {
  mostrarDiv: boolean = false;
  nombreIncompleto: boolean = false;
  emailIncompleto: boolean = false;
  asuntoIncompleto: boolean = false;
  mensajeIncompleto: boolean = false;
  completo: boolean = true;
  contacto: FormGroup;
  respuesta: string = '';
  resp: boolean = true;

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.contacto = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      nombre: ['', Validators.required],
      mensaje: ['', Validators.required],
      asunto: ['', Validators.required],
    })
  }

  ngOnInit(): void {
    setTimeout(() => {
      this.mostrarDiv = true;
    }, 200);
  }

  sendEmail() {
    if (this.contacto.valid){
      this.http.post('http://127.0.0.1:8000/send_email/', this.contacto.value).subscribe(
        (response) => {
          console.log('Correo electrónico enviado correctamente', response);
          this.respuesta = '¡Correo electrónico enviado correctamente!';
          this.resp = false;
        },
        (error) => {
          console.error('Error al enviar el correo electrónico', this.contacto.value);
          this.respuesta = 'No se pudo enviar el correo electrónico, intente más tarde';
          this.resp = false;
        }
      );
    }
    else {
      this.resp = true;
      this.nombreIncompleto = this.contacto.value.nombre == '';
      this.emailIncompleto = this.contacto.value.email == '';
      this.asuntoIncompleto = this.contacto.value.asunto == '';
      this.mensajeIncompleto = this.contacto.value.mensaje == '';
      this.completo = false;
    }
  }
}
