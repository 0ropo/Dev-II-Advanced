import unittest

if __name__ == "__main__":
    # Définissez le répertoire contenant vos tests
    test_dir = 'test'
    # Créez un loader de tests
    test_loader = unittest.TestLoader()
    # Découvrez tous les tests dans le répertoire spécifié
    test_suite = test_loader.discover(test_dir)
    # Exécutez les tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
