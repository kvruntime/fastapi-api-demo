/*
  Warnings:

  - You are about to drop the column `authorId` on the `Post` table. All the data in the column will be lost.
  - The primary key for the `User` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - A unique constraint covering the columns `[author_id]` on the table `Post` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `author_id` to the `Post` table without a default value. This is not possible if the table is not empty.
  - Changed the type of `id` on the `User` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- DropForeignKey
ALTER TABLE "Post" DROP CONSTRAINT "Post_authorId_fkey";

-- DropIndex
DROP INDEX "Post_authorId_key";

-- AlterTable
ALTER TABLE "Post" DROP COLUMN "authorId",
ADD COLUMN     "author_id" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "User" DROP CONSTRAINT "User_pkey",
ADD COLUMN     "birth_date" TIMESTAMP(3),
ADD COLUMN     "is_verified" BOOLEAN NOT NULL DEFAULT false,
ADD COLUMN     "nickname" TEXT,
ADD COLUMN     "phone" TEXT,
ADD COLUMN     "photo_url" TEXT,
DROP COLUMN "id",
ADD COLUMN     "id" UUID NOT NULL,
ADD CONSTRAINT "User_pkey" PRIMARY KEY ("id");

-- CreateIndex
CREATE UNIQUE INDEX "Post_author_id_key" ON "Post"("author_id");

-- AddForeignKey
ALTER TABLE "Post" ADD CONSTRAINT "Post_author_id_fkey" FOREIGN KEY ("author_id") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
