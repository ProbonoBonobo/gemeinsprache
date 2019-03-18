from gemeinsprache.shell import ExecutableShellCommand

basic_cmd = ExecutableShellCommand("echo 'Hello!'")
bad_cmd = ExecutableShellCommand("sl")

class TestClass_ExecutableShellCommand():
    
    def test_return_object_has_expected_exit_code(self):
        assert basic_cmd.exit_code == 0
        assert bad_cmd.exit_code > 0
