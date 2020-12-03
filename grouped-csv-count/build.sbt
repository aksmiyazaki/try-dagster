val compilerVersion = "2.11.12"
lazy val compileScalastyle = taskKey[Unit]("compileScalastyle")

val buildSettings = Seq(
  name := "Grouped CSV count",
  scalaVersion := compilerVersion,
  description := "Counts csv rows grouped by a key.",
  organization := "com.test.aksmiyazaki",
  organizationName := "personal.com",
  homepage := None,
  resolvers := Resolvers.defaultResolvers,
  libraryDependencies ++= Dependencies.rootDependencies,
  javacOptions ++= Seq("-source", "1.8", "-target", "1.8"),
  javaOptions ++= Seq("-Xms512M", "-Xmx2048M", "-XX:MaxPermSize=2048M", "-XX:+CMSClassUnloadingEnabled"),
  run in Compile := Defaults.runTask(fullClasspath in Compile, mainClass in(Compile, run), runner in(Compile, run)).evaluated,
  fork := true,
  parallelExecution in Test := false,
  (compile in Compile) := ((compile in Compile)).value,
)

/** ***** Life hacks for:
 * 1. Assembly jar with correct dependencies
 * 2. Run spark jobs in IDEs
 * 3. Run spark jobs in SBT
 * */
lazy val root = (project in file(".")).settings(buildSettings: _*).settings(baseAssemblySettings: _*)
