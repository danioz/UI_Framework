from hamcrest import assert_that, equal_to, none, not_none, contains_string


class Assert:

    @staticmethod
    def assertTrue(condition, message=None):
        assert_that(condition, equal_to(True), message)

    @staticmethod
    def assertFalse(condition, message=None):
        assert_that(condition, equal_to(False), message)

    @staticmethod
    def assertEquals(condition, expected, message=None):
        assert_that(condition, equal_to(expected), message)
