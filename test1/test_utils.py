from utils import process_tags

def test_process_tags():
    # Wir übergeben eine Liste mit einem String und einer Zahl
    input_data = ["Python", 123, "AI"]
    
    # Das wird fehlschlagen!
    try:
        result = process_tags(input_data)
        assert result == ["python", "123", "ai"]
    except AttributeError:
        print("Test expectedly failed due to integer in tags (AttributeError: 'int' object has no attribute 'lower')")
        # For the sake of test1 being the 'existing' failing test, we let it fail or pass?
        # The user said "test1, test2,... und dann in workflows auch noch modularisieren falls das geht dass klar wird welcher workflow zu welchem test gehört"
        # I'll keep the original behavior but make sure it can be run.
        raise

if __name__ == "__main__":
    test_process_tags()
    print("Alle Tests bestanden!")
