def main():
    mass_kg = int(input("Mass in kilograms: "))
    energy_joules = compute_energy(mass_kg)
    print(energy_joules)


def compute_energy(mass_kg):
    # c = 300_000_000
    c = 3e8
    energy_joules = mass_kg * c**2
    return int(energy_joules)


if __name__ == "__main__":
    main()