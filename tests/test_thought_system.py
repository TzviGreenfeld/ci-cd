from click.testing import CliRunner
from thought_system.__main__ import main


def test_br():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert "Usage: main [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "--help  Show this message and exit." in result.output
    assert "Commands:" in result.output
    assert "serve" in result.output
    assert "serve-web" in result.output
    assert "upload-thought" in result.output
