/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package actividad1.java;

import Clases.Animal;
import java.time.LocalDate;

/**
 *
 * @author Didier
 */
public class ACTIVIDAD1JAVA {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
          Animal miMascota = new Animal(
            "Sparky",
            12.5,
            "Didier",
            LocalDate.of(2020, 5, 14),
            LocalDate.of(2023, 11, 20)
        );
          
        miMascota.mostrarInfo();

        miMascota.setPeso(13.2);
        miMascota.setFechaUltimaVacuna(LocalDate.of(2024, 1, 15));

        System.out.println("\n--- Informacion actualizada ---");
        miMascota.mostrarInfo();
    }
    
}
