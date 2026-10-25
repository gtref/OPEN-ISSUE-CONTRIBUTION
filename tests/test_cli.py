from Training.cli import main


def test_string_length(capsys):
    main(["--string-length", "15"])
    assert "The length of the string is: 2" in capsys.readouterr().out


def test_string_length_accepts_text(capsys):
    main(["--string-length", "hello"])
    assert "The length of the string is: 5" in capsys.readouterr().out


def test_version(capsys):
    try:
        main(["--version"])
    except SystemExit as error:
        assert error.code == 0
    assert "Training 0.1.0" in capsys.readouterr().out


def test_no_arguments_shows_help(capsys):
    main([])
    output = capsys.readouterr().out
    assert "usage:" in output
    assert "--string-length" in output
    assert "The length of the string is:" not in output


def test_empty_string_reports_zero(capsys):
    main(["--string-length", ""])
    assert "The length of the string is: 0" in capsys.readouterr().out


def test_generate_password_cli(capsys):
    main(["--generate-password"])
    assert "Generated password:" in capsys.readouterr().out


def test_length_sets_generated_password_size(capsys):
    main(["--generate-password", "--length", "8"])

    output = capsys.readouterr().out
    assert output.startswith("Generated password: ")
    password = output[len("Generated password: ") :].rstrip("\n")
    assert len(password) == 8


def test_length_without_generate_password_does_not_generate(capsys):
    main(["--length", "8"])

    assert capsys.readouterr().out == ""
