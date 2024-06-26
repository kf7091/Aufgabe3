from calculation import calc_mean
import my_functions as mf

if __name__ == "__main__":
   subject = mf.build_person(
      input("Geben Sie den Vornamen des Probande:in ein:"),
      input("Geben Sie den Nachnamen des Probande:in ein:"),
      input("Geben sie das Geschlecht 'male' oder 'female' an:"),
      int(input("Geben Sie das Alter des Probande:in ein:"))
   )
   supervisor = mf.build_person(
      input("Geben Sie den Vornamen des Supervisors ein:"),
      input("Geben Sie den Nachnamen des Supervisors ein:"),
      input("Geben sie das Geschlecht des Supervisors 'male' oder 'female' an:"),
      int(input("Geben Sie das Alter des Supervisors ein:"))
    )
            
experiment = mf.build_experiment(
    input("Geben Sie den Experimentnamen ein:"),
    input("Geben Sie das Datum ein:"),
    supervisor,
    subject
   )
print(experiment)