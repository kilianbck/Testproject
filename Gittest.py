def is_even(number):
    """Prüft, ob eine Zahl gerade ist."""
    return number % 2 == 0

# Testfunktion
def test_is_even():
    assert is_even(2) == True, "2 sollte als gerade erkannt werden"
    assert is_even(3) == False, "3 sollte als ungerade erkannt werden"
    assert is_even(0) == True, "0 sollte als gerade erkannt werden"
    assert is_even(-4) == True, "-4 sollte als gerade erkannt werden"
    assert is_even(-3) == False, "-3 sollte als ungerade erkannt werden"

# Test ausführen
if __name__ == "__main__":
    test_is_even()
    print("Alle Tests erfolgreich bestanden!")