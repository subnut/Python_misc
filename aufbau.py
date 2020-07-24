# Aufbau
class Aufbau:
    def __init__(self, args=None):
        if args is not None:
            self.update_input(args)

    def update_input(self, args=None):
        if args is not None:
            if isinstance(args, str):
                self.global_orbital_list = args
                self.generate_from_orbital_list()
            if isinstance(args, int):
                self.global_last_orbit = args
                self.generate_from_last_orbit()

    def generate_from_orbital_list(self, orbital_list=None):
        if not orbital_list:
            try:
                orbital_list = self.global_orbital_list
            except NameError:
                raise NameError("Orbital list not defined")
        orbit_list = [None]
        for orbit_no in range(1, 2 * len(orbital_list) + 1):
            orbit_list.append(str(orbit_no))
        self.global_orbit_list = orbit_list
        self.generate_output()

    def generate_from_last_orbit(self, last_orbit=None):
        if not last_orbit:
            try:
                last_orbit = self.global_last_orbit
            except NameError:
                raise NameError("Last orbit number not specified")
        if last_orbit not in range(1, 25):
            print("Last orbit must be an integer from 1 to 24")
            return
        if last_orbit % 2 != 0:
            print(
                """WARNING: Provided outermost orbital number is odd
Rounding off to next even number ..."""
            )
        last_orbit = (last_orbit + 1) // 2
        self.global_orbital_list = "spdfghijklmnopqrstuvwxyz"[:last_orbit]
        self.generate_from_orbital_list()

    def generate_output(self):
        orbital_list = self.global_orbital_list
        orbit_list = self.global_orbit_list
        return_list = []
        for current_energy in range(1, 2 * len(orbital_list) + 1):
            for current_orbit_energy in range(len(orbit_list)):
                for current_orbital_energy in range(current_orbit_energy):
                    if (
                        current_orbit_energy + current_orbital_energy
                        == current_energy
                    ):
                        return_list.append(
                            orbit_list[current_orbit_energy]
                            + orbital_list[current_orbital_energy]
                        )
                        break
                    break
        self.global_output = return_list

    def print_list(self):
        for orbital in self.global_output:
            print(orbital)

    def print_chart(self):
        for orbit in self.global_orbit_list:
            for orbital in self.global_output:
                if orbital[:-1] == str(orbit):
                    if len(self.global_orbit_list[-1]) > 1 & len(orbital) < 3:
                        print("0" + orbital, end=" ")
                    else:
                        print(orbital, end=" ")
            if orbit and int(orbit) > len(self.global_orbital_list):
                print("...", end=" ")
            print()
        print()


def main(user_object):
    print(
        """What do you have?
1. Orbital List
2. Last Orbit number"""
    )
    user_input = input("Enter your option: ")
    if user_input not in ("1", "2"):
        print("Invalid option!")
        return
    elif user_input == "1":
        user_input = input(
            "Please enter the order of the orbitals WITHOUT whitespace: "
        )
    elif user_input == "2":
        user_input = input("Please enter the last orbit number: ")
        if not user_input.isalnum():
            print("Invalid number")
            return
        user_input = int(user_input)
    user_object.update_input(user_input)
    print(
        """What do you want to print?
1. Aufbau Chart
2. Aufbau List"""
    )
    user_input = input("Enter your option: ")
    if user_input not in ("1", "2"):
        print("Invalid option!")
        return
    elif user_input == "1":
        user_object.print_chart()
    elif user_input == "2":
        user_object.print_list()


if __name__ == "__main__":
    user_object = Aufbau()
    print("To quit, press Ctrl-C anytime")
    while True:
        try:
            main(user_object)
        except KeyboardInterrupt:
            print("\nExiting ...")
            break
